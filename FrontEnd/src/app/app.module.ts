import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FooterComponent } from './components/footer/footer.component';
import { HeaderComponent } from './components/header/header.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { MainComponent } from './components/main/main.component';
import { InterceptorService } from './services/interceptor-service/interceptor-service.service';
import { ErrorComponent } from './components/error/error/error.component';
import { UsersGestionComponent } from './components/users-gestion/users-gestion.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material-module';
import { HostsGestionComponent } from './components/hosts-gestion/hosts-gestion.component';
import { InfraestructuraComponent } from './components/infraestructura/infraestructura.component';
import { ModalHostComponent } from './components/modal-host/modal-host.component';
import { ModalNewHostComponent } from './components/modal-new-host/modal-new-host.component';

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    HeaderComponent,
    LoginComponent,
    RegisterComponent,
    SidebarComponent,
    MainComponent,
    ErrorComponent,
    UsersGestionComponent,
    HostsGestionComponent,
    InfraestructuraComponent,
    ModalHostComponent,
    ModalNewHostComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: InterceptorService,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
