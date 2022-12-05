import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserService } from 'src/app/services/user/user.service';
import { UsersGestionComponent } from '../users-gestion/users-gestion.component';

@Component({
  selector: 'app-modal-new-user',
  templateUrl: './modal-new-user.component.html',
  styleUrls: ['./modal-new-user.component.css']
})
export class ModalNewUserComponent implements OnInit {

  newUserForm!: FormGroup;
  name = '';
  surname = '';
  email = '';
  username = '';
  password = '';
  noData = false;
  @ViewChild('closebutton') closebutton: any;

  constructor(
    private fb: FormBuilder,
    private userService: UserService,
    private userComponent: UsersGestionComponent
  ) { }

  ngOnInit(): void {
    this.newUserForm = this.fb.group({
      name: [null, Validators.required],
      surname: [null, Validators.required],
      email: [null, Validators.required],
      username: [null, Validators.required],
      password: [null, Validators.required],
    });
  }

  createUser(): void {
    if ((this.newUserForm.value.name === null || this.newUserForm.value.surname === null || this.newUserForm.value.email === null || this.newUserForm.value.username === null || this.newUserForm.value.password === null) 
    || (this.newUserForm.value.name === "" || this.newUserForm.value.surname === "" || this.newUserForm.value.email === "" || this.newUserForm.value.username === "" || this.newUserForm.value.password === "")) {
      this.noData = true;
    } else {
      this.noData = false;
      this.userService.createUser(this.newUserForm.value).subscribe({
        next: (res: any) => {
          this.closebutton.nativeElement.click();
          this.userComponent.getUsers();
        },
        error: (e) => {
          // Redirigir a la pagina de error
        }
      });
    }
  }
}
