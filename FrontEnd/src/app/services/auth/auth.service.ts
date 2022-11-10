import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { buffer, catchError, Observable, tap, throwError } from 'rxjs';
import { ApiService } from '../api/api.service';
import { TokenService } from '../token/token.service';

const OAUTH_CLIENT = 'current-user';
const OAUTH_SECRET = 'secret';
const API_URL = 'http://127.0.0.1:8000/api/';
const HTTP_OPTIONS = {
    headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
    })
};

@Injectable({
    providedIn: 'root'
})
export class AuthService {
    private static handleError(error: HttpErrorResponse): any {
        if (error.error instanceof ErrorEvent) {
            console.error('An error occured: ', error.error.message);
        } else {
            console.error(
                `Backend returned code ${error.status}`,
                `body was: ${error.error}`
            );
        }
        return throwError(() => new Error(
            'Something bad Hapenned: please try again later.'
            ) 
        );
    }

    private static log(message: string): any {
        console.log(message);
    }

    constructor(private http: HttpClient, 
        private tokenService: TokenService,
        private router: Router) {
    }

    login(loginData: any): Observable<any> {
        this.tokenService.removeToken();
        const body = new HttpParams()
            .set('username', loginData.username)
            .set('password', loginData.password)
            .set('grant_type', 'password');
        return this.http.post<any>(API_URL + 'user/login', body, HTTP_OPTIONS).pipe(
            tap(res => {
                this.tokenService.saveToken(res.access_token);
            }),
            catchError((error: HttpErrorResponse) => {
                return throwError(() => new Error(error.message));
              })
          );
    }    

    logout(): void {
        this.tokenService.removeToken();
    }

    register(data: any): Observable<any> {
        return this.http.post<any>(API_URL + '/user/signin', data).pipe(tap({
            next: (v: any) => {
                AuthService.log(v);
            }, 
            error: (e) => AuthService.handleError(e)
        }));
    }
}