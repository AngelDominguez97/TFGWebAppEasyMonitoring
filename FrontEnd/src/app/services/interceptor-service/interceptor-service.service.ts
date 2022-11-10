import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpRequest, HttpResponse, HttpErrorResponse, HttpInterceptor } from '@angular/common/http';
import { Observable, Subject, of, throwError, map, catchError } from 'rxjs';
import { Router } from '@angular/router';

import { AuthService } from '../auth/auth.service';
import { TokenService } from '../token/token.service';

@Injectable({
  providedIn: 'root'
})
export class InterceptorService implements HttpInterceptor{

  constructor(
    private router: Router,
    private tokenService: TokenService,
    private authService: AuthService
  ) {}
  intercept(request: HttpRequest<any>, next: HttpHandler): any {
    const token = this.tokenService.getToken();
    if (token) {
      request = request.clone({
        setHeaders: {
          Authorization: 'Bearer ' + token
        }
      });
    }

    if (!request.headers.has('Content-Type')){
      request = request.clone({
        setHeaders: {
          'Content-Type': 'application/json'
        }
      });
    }

    request = request.clone({
      headers: request.headers.set('Accept', 'application/json')
    });

    return next.handle(request).pipe(map((event: HttpEvent<any>) => {
      if (event instanceof HttpResponse) {
        console.log('event--->>>', event);
      }
      return event
      }),
      catchError((error: HttpErrorResponse) => {
        debugger;
        if (error.status === 401) {
          if (error.error.detail === 'invalid_token') {
            this.authService.logout();
            this.router.navigate(['/login']);
          }
        }
        return throwError(() => new Error(error.status.toString()));
      })
    )
  }
}