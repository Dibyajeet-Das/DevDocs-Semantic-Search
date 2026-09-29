import { ApplicationConfig } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [provideHttpClient()],
};

// Base URL of the FastAPI backend (uvicorn default).
export const API_BASE_URL = 'http://localhost:8000';
