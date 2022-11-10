import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth/auth.service';

export class MyErrorStateMatcher implements MyErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  username = '';
  password = '';
  noData = false;
  wrongCredentials = false;
  matcher = new MyErrorStateMatcher();

  constructor(
    private authService: AuthService, 
    private router: Router, 
    private formBuilder: FormBuilder
    ) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      username : [null, Validators.required],
      password : [null, Validators.required]
    });
  }

  onFormSubmit(): void {
    if (this.loginForm.value.username === null || this.loginForm.value.password === null){
      this.noData = true;
    } else {
      this.noData = false;
      this.authService.login(this.loginForm.value)
      .subscribe({
        next: (v: any) => {
          this.router.navigate(['main'])
        }, 
        error: (e) => {
          if (e.message === '401'){
            this.wrongCredentials = true;
          }
        }
      });
    }
  }
}