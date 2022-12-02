import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { UserModel } from 'src/app/models/user.model';

const API_URL = 'http://127.0.0.1:8000/api/';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  
  users!: UserModel[]

  constructor(
    private http: HttpClient,
  ) { }

  getUsers(): Observable<UserModel[]>{
    return this.http.get<any>(API_URL + 'user/allusers').pipe(
      tap(res => {
        this.users = res;
      }),
      catchError((error: HttpErrorResponse) => {
          return throwError(() => new Error(error.message));
        })
    ) as Observable<UserModel[]>;
  }

  deleteUserById(id: number): Observable<any> {
    return this.http.delete(API_URL + 'user/delete/' + id).pipe(
      tap(res => {
        alert(res);
      }),
      catchError((error: HttpErrorResponse) => {
        return throwError(() => new Error(error.message));
      })
    );
  }
}
