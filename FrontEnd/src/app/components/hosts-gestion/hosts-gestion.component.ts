import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { HostModel } from 'src/app/models/host.model';
import { HostService } from 'src/app/services/host/host.service';
import { PreviousRouteService } from 'src/app/services/previous-route/previous-route.service';
import { ModalHostComponent } from '../modal-host/modal-host.component';

@Component({
  selector: 'app-hosts-gestion',
  templateUrl: './hosts-gestion.component.html',
  styleUrls: ['./hosts-gestion.component.css']
})
export class HostsGestionComponent implements OnInit {

  displayedColumns: string[] = ['id', 'hostName', 'hostIp', 'userId', 'action'];
  hosts!: HostModel[];
  dataSource!: any;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(
    private hostService: HostService,
    private previousRouteService: PreviousRouteService,
    public dialog: MatDialog,
    ) { }
  
    ngOnInit(): void {
      this.getHosts();
    }

    public getHosts() {
      this.hostService.getHosts()
      .subscribe({
        next: (res: any) => {
          this.hosts = res;
          this.dataSource = new MatTableDataSource<HostModel>(this.hosts);
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
    const dialog = this.dialog.open(ModalHostComponent, {
      width: '250px',
      // Can be closed only by clicking the close button
      disableClose: true,
      data: element
    });
  }

  functionDelete(id: number){
    this.hostService.deleteHostById(id).subscribe({
      next: (res: any) => {
        this.getHosts();
      }, 
      error: (e) => {
        // Redirigir a la pagina de error
      }
    }); 
  }

}