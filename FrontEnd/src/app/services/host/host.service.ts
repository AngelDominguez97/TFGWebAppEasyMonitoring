import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { HostModel } from 'src/app/models/host.model';

const API_URL = 'http://127.0.0.1:8000/api/';
const HTTP_OPTIONS = {
  headers: new HttpHeaders({
      'Content-Type': 'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class HostService {
  
  hosts!: HostModel[]

  constructor(
    private http: HttpClient,
  ) { }

  getHosts(): Observable<HostModel[]>{
    return this.http.get<any>(API_URL + 'allhosts').pipe(
      tap(res => {
        this.hosts = res;
      }),
      catchError((error: HttpErrorResponse) => {
          return throwError(() => new Error(error.message));
        })
    ) as Observable<HostModel[]>;
  }

  createHost(hostData: any){
    return this.http.post(API_URL + 'host/', hostData, HTTP_OPTIONS).pipe(
      tap(res => {
        alert("The host was created successfully.");
      }),
      catchError((error: HttpErrorResponse) => {
        return throwError(() => new Error(error.message));
      })
    );
  }

  deleteHostById(id: number): Observable<any> {
    return this.http.delete(API_URL + 'host/delete' + id).pipe(
      tap(res => {
        alert(res);
      }),
      catchError((error: HttpErrorResponse) => {
        return throwError(() => new Error(error.message));
      })
    );
  }

  updateHost(hostData: any){
    return this.http.post(API_URL + 'host/update', hostData, HTTP_OPTIONS).pipe(
      tap(res => {
        alert(res);
      }),
      catchError((error: HttpErrorResponse) => {
        return throwError(() => new Error(error.message));
      })
    );
  }
}
