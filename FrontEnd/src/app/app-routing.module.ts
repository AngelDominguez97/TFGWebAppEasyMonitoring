import { NgModule } from '@angular/core';
import { LoginComponent } from './components/login/login.component';
import { MainComponent } from './components/main/main.component';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuardService } from './services/auth-guard/auth-guard.service';
import { ErrorComponent } from './components/error/error/error.component';
import { UsersGestionComponent } from './components/users-gestion/users-gestion.component';
import { HostsGestionComponent } from './components/hosts-gestion/hosts-gestion.component';
import { InfraestructuraComponent } from './components/infraestructura/infraestructura.component';

const routes: Routes = [
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'main',
    component: MainComponent,
    canActivate: [AuthGuardService]
  },
  {
    path: 'infraestructura',
    component: InfraestructuraComponent,
    canActivate: [AuthGuardService]
  },
  {
    path: 'users/Gestion',
    component: UsersGestionComponent,
    canActivate: [AuthGuardService]
  },
  {
    path: 'hosts/Gestion',
    component: HostsGestionComponent,
    canActivate: [AuthGuardService]
  },
  { 
    path: '', 
    component: MainComponent,
    canActivate: [AuthGuardService]
  },
  { 
    path: '**', 
    component: ErrorComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
