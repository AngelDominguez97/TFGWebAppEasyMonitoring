import { Component, OnInit } from '@angular/core';
import { Router} from '@angular/router';
import { AuthService } from 'src/app/services/auth/auth.service';
import { PreviousRouteService } from 'src/app/services/previous-route/previous-route.service';
import { TokenService } from 'src/app/services/token/token.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  constructor(
    private authService: AuthService,
    private tokenService: TokenService,
    private router: Router,
    private previousRouteService: PreviousRouteService
  ) { }

  ngOnInit(): void {
  }

  reloadIfComesFromLogIn() {
    if (this.previousRouteService.getPreviousUrl() !== this.previousRouteService.getCurrentUrl()){
      window.location.reload();
    }
  }
}
