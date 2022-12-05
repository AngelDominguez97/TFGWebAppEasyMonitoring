import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { UserModel } from 'src/app/models/user.model';
import { PreviousRouteService } from 'src/app/services/previous-route/previous-route.service';
import { UserService } from 'src/app/services/user/user.service';
import { ModalUserComponent } from '../modal-user/modal-user.component';

@Component({
  selector: 'app-users-gestion',
  templateUrl: './users-gestion.component.html',
  styleUrls: ['./users-gestion.component.css']
})
export class UsersGestionComponent implements OnInit{

  displayedColumns: string[] = ['id', 'username', 'name', 'surname', 'email', 'action'];
  users!: UserModel[];
  dataSource!: any;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(
    private userService: UserService,
    private previousRouteService: PreviousRouteService,
    public dialog: MatDialog,
    ) { }
  
    ngOnInit(): void {
      this.getUsers();
    }

  getUsers() {
    this.userService.getUsers()
    .subscribe({
      next: (res: any) => {
        this.users = res;
        this.dataSource = new MatTableDataSource<UserModel>(this.users);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      }, 
      error: (e) => {
        // Redirigir a la pagina de error
      }
    });  
  }

  filterChange(event: Event){
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue;
  }

  functionEdit(element: any){
    debugger;
    const dialog = this.dialog.open(ModalUserComponent, {
      width: '250px',
      disableClose: true,
      data: element
    });
  }

  functionDelete(id: number){
    this.userService.deleteUserById(id).subscribe({
      next: (res: any) => {
        this.getUsers();
      }, 
      error: (e) => {
        // Redirigir a la pagina de error
      }
    }); 
  }

}