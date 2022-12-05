import { Component, Inject, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-modal-user',
  templateUrl: './modal-user.component.html',
  styleUrls: ['./modal-user.component.css']
})
export class ModalUserComponent implements OnInit {

  updateUserForm!: FormGroup;
  id = 0;
  name = '';
  surname = '';
  email = '';
  username = '';
  noData = false;
  
  constructor(
      private userService: UserService,
      public dialogRef: MatDialogRef<ModalUserComponent>,
      private fb: FormBuilder,
      @Inject(MAT_DIALOG_DATA) public data: any
  ) { 
      this.id = data.id;
      this.name = data.name;
      this.surname = data.surname;
      this.email = data.email;
      this.username = data.username;
  }


  ngOnInit() {
    this.updateUserForm = this.fb.group({
        id: [this.id, []],
        name: [this.name, []],
        surname: [this.surname, []],
        email: [this.email, []],
        username: [this.username, []]
    });
  }

  closeDialog() {
      this.dialogRef.close();
  }

  updateHost(): void {
      if ((this.updateUserForm.value.name === null || this.updateUserForm.value.surname === null || this.updateUserForm.value.email === null || this.updateUserForm.value.username === null) 
      || (this.updateUserForm.value.name === "" || this.updateUserForm.value.surname === "" || this.updateUserForm.value.email === "" || this.updateUserForm.value.username === "")) {
          this.noData = true;
      } else {
          this.noData = false;
          this.userService.updateUser(this.updateUserForm.value).subscribe({
              next: (res: any) => {

              },
              error: (e) => {
                  // Redirigir a la pagina de error
              }
          });
      }
  }
}
