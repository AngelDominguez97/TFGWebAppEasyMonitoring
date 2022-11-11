import { Component, OnInit } from '@angular/core';
import { UserModel } from 'src/app/models/user.model';
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  user!: UserModel;

  constructor(
      public authService: AuthService,
    ) { 
      this.me();
    }

  ngOnInit(): void {
  }

  me(): void{
    this.authService.me()
    .subscribe({
      next: (v: any) => {
        this.user = v as UserModel;
      }, 
      error: (e) => {
        // Redirigir a la pagina de error
      }
    });
  }
}
