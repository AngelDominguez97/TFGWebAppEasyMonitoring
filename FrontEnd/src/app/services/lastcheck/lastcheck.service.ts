import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { LastCheckModel } from 'src/app/models/lastcheck.model';

const API_URL = 'http://127.0.0.1:8000/api/';

@Injectable({
  providedIn: 'root'
})
export class LastcheckService {
  
  lastCheck!: LastCheckModel[]

  constructor(
    private http: HttpClient,
  ) { }

  getAllLastChecks(): Observable<LastCheckModel[]>{
    return this.http.get<any>(API_URL + 'checksHandler/getallchecks').pipe(
      tap(res => {
        this.lastCheck = res;
      }),
      catchError((error: HttpErrorResponse) => {
          return throwError(() => new Error(error.message));
        })
    ) as Observable<LastCheckModel[]>;
  }
}
