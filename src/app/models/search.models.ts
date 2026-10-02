export interface SearchResult {
  id: string;
  title: string;
  category: string;
  source: string;
  content: string;
  /** 0..1 where higher = more similar; null when the API gives no score. */
  similarity: number | null;
}

export const CATEGORIES = [
  { value: '', label: 'All categories' },
  { value: 'spring', label: 'Spring' },
  { value: 'python', label: 'Python' },
  { value: 'kafka', label: 'Kafka' },
  { value: 'docker', label: 'Docker' },
];

/** Turns "spring_boot.txt" into "Spring Boot". */
function prettify(name: string): string {
  return name
    .replace(/\.[a-z0-9]+$/i, '')
    .replace(/[_-]+/g, ' ')
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

function clamp(n: number): number {
  return Math.max(0, Math.min(1, n));
}

function toSimilarity(item: any): number | null {
  if (typeof item.similarity === 'number') return clamp(item.similarity);
  if (typeof item.score === 'number') return clamp(item.score);
  if (typeof item.distance === 'number') return clamp(1 - item.distance); // cosine distance -> similarity
  return null;
}

function toResult(item: any, index: number): SearchResult {
  const meta = item.metadata ?? {};
  const source = meta.source ?? meta.filename ?? meta.file ?? item.source ?? '';
  const category = meta.category ?? item.category ?? '';
  return {
    id: String(item.id ?? `${source}-${index}`),
    title: meta.title ?? item.title ?? (source ? prettify(source) : prettify(category || 'Document')),
    category,
    source,
    content: item.document ?? item.text ?? item.content ?? item.chunk ?? '',
    similarity: toSimilarity(item),
  };
}

/**
 * Accepts the response shapes a FastAPI + ChromaDB backend commonly returns:
 *  - [ {document, metadata, distance}, ... ]
 *  - { results: [ ... ] }
 *  - raw Chroma: { ids:[[]], documents:[[]], metadatas:[[]], distances:[[]] }
 */
export function normalizeResponse(body: any): SearchResult[] {
  if (!body) return [];
  if (Array.isArray(body)) return body.map(toResult);
  if (Array.isArray(body.results)) return body.results.map(toResult);

  if (Array.isArray(body.documents)) {
    const docs: string[] = body.documents[0] ?? [];
    const metas: any[] = body.metadatas?.[0] ?? [];
    const dists: number[] = body.distances?.[0] ?? [];
    const ids: string[] = body.ids?.[0] ?? [];
    return docs.map((document, i) =>
      toResult({ id: ids[i], document, metadata: metas[i], distance: dists[i] }, i),
    );
  }
  return [];
}
