import { Component, OnInit, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpErrorResponse } from '@angular/common/http';
import { SearchService } from './services/search.service';
import { CATEGORIES, SearchResult } from './models/search.models';
import { ResultCardComponent } from './components/result-card/result-card.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, ResultCardComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit {
  private api = inject(SearchService);

  readonly categories = CATEGORIES;
  readonly topKOptions = [1, 3, 5, 10];
  readonly examples = [
    'How does Spring manage objects?',
    'How does Python run my code?',
    'Package an app so it runs anywhere',
    'How do services exchange streams of events?',
  ];

  query = '';
  category = '';
  topK = 3;

  results = signal<SearchResult[]>([]);
  loading = signal(false);
  error = signal<string | null>(null);
  searched = signal(false);
  backendUp = signal<boolean | null>(null);
  lastQuery = signal('');

  ngOnInit(): void {
    this.api.health().subscribe({
      next: (h) => this.backendUp.set(h?.status === 'UP'),
      error: () => this.backendUp.set(false),
    });
  }

  useExample(text: string): void {
    this.query = text;
    this.search();
  }

  search(): void {
    const q = this.query.trim();
    if (!q) {
      this.error.set('Enter a question to search the docs.');
      return;
    }
    this.error.set(null);
    this.loading.set(true);

    this.api.search(q, this.topK, this.category).subscribe({
      next: (res) => {
        this.results.set(res);
        this.lastQuery.set(q);
        this.searched.set(true);
        this.loading.set(false);
      },
      error: (err: HttpErrorResponse) => {
        this.results.set([]);
        this.loading.set(false);
        this.error.set(this.describe(err));
      },
    });
  }

  private describe(err: HttpErrorResponse): string {
    if (err.status === 0) {
      return 'Cannot reach the API at localhost:8000. Start FastAPI with uvicorn and check that CORS is enabled.';
    }
    if (err.status === 422) return 'The API rejected the request. Check the query and result count.';
    if (err.status >= 500) return 'The API hit an error while searching. Check the FastAPI logs.';
    return `Search failed (HTTP ${err.status}).`;
  }
}
