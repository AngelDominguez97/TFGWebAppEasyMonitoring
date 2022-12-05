import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, tap, throwError } from 'rxjs';
import { UserModel } from 'src/app/models/user.model';

const API_URL = 'http://127.0.0.1:8000/api/';
const HTTP_OPTIONS = {
  headers: new HttpHeaders({
      'Content-Type': 'application/json'
  })
};

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

  createUser(userData: any){
    debugger;
    return this.http.post(API_URL + 'user/signin', userData, HTTP_OPTIONS).pipe(
      tap(res => {
        alert("The user was created successfully.");
      }),
      catchError((error: HttpErrorResponse) => {
        return throwError(() => new Error(error.message));
      })
    );
  }

  updateUser(userData: any){
    return this.http.post(API_URL + 'user/update', userData, HTTP_OPTIONS).pipe(
      tap(res => {
        alert(res);
      }),
      catchError((error: HttpErrorResponse) => {
        return throwError(() => new Error(error.message));
      })
    );
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
