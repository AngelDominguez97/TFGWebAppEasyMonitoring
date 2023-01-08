import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { retry } from 'rxjs';
import { LastCheckModel } from 'src/app/models/lastcheck.model';
import { HostService } from 'src/app/services/host/host.service';
import { LastcheckService } from 'src/app/services/lastcheck/lastcheck.service';
import { PreviousRouteService } from 'src/app/services/previous-route/previous-route.service';
import { ModalHostMonitorComponent } from '../modal-host-monitor/modal-host-monitor.component';

@Component({
  selector: 'app-infraestructura',
  templateUrl: './infraestructura.component.html',
  styleUrls: ['./infraestructura.component.css']
})
export class InfraestructuraComponent implements OnInit {

  displayedColumns: string[] = ['hostName', 'hostIp', 'ping', 'cpuUsage', 'ramUsed', 'ramFree', 'ramCached', 'netIn', 'netOut', 'Info'];
  lastCheck!: LastCheckModel[];
  dataSource!: any;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(
    private lastCheckService: LastcheckService,
    private previousRouteService: PreviousRouteService,
    public dialog: MatDialog,
    ) { }
  
    ngOnInit(): void {
      this.getAllLastChecks();
    }

    getAllLastChecks() {
      this.lastCheckService.getAllLastChecks()
      .subscribe({
        next: (res: any) => {
          this.lastCheck = res;
          this.dataSource = new MatTableDataSource<LastCheckModel>(this.lastCheck);
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
    const dialog = this.dialog.open(ModalHostMonitorComponent, {
      width: '1000px',
      disableClose: true,
      data: element
    });
  }

  functionDelete(id: number){

  }

  getStatus(element: any){
    if (element.ping === 'UP') {
      return true;
    } else {
      return false;
    }
  }

}