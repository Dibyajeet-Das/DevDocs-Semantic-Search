import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { API_BASE_URL } from '../app.config';
import { SearchResult, normalizeResponse } from '../models/search.models';

@Injectable({ providedIn: 'root' })
export class SearchService {
  private http = inject(HttpClient);

  search(query: string, topK: number, category: string): Observable<SearchResult[]> {
    let params = new HttpParams().set('query', query).set('top_k', topK);
    if (category) params = params.set('category', category);

    return this.http
      .get<unknown>(`${API_BASE_URL}/search`, { params })
      .pipe(map((body) => normalizeResponse(body)));
  }

  health(): Observable<{ status: string }> {
    return this.http.get<{ status: string }>(`${API_BASE_URL}/health`);
  }
}
