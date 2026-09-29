import { Component, Input, signal } from '@angular/core';
import { SearchResult } from '../../models/search.models';

@Component({
  selector: 'app-result-card',
  standalone: true,
  templateUrl: './result-card.component.html',
  styleUrl: './result-card.component.css',
})
export class ResultCardComponent {
  @Input({ required: true }) result!: SearchResult;
  @Input() rank = 1;

  expanded = signal(false);
  readonly limit = 320;

  get isLong(): boolean {
    return this.result.content.length > this.limit;
  }

  get text(): string {
    return this.expanded() || !this.isLong
      ? this.result.content
      : this.result.content.slice(0, this.limit).trimEnd() + '…';
  }

  get percent(): number {
    return Math.round((this.result.similarity ?? 0) * 100);
  }

  toggle(): void {
    this.expanded.update((v) => !v);
  }
}
