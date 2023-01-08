import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-modal-host-monitor',
  templateUrl: './modal-host-monitor.component.html',
  styleUrls: ['./modal-host-monitor.component.css']
})
export class ModalHostMonitorComponent implements OnInit {

  hostIp = '';
  srcIframe = '';

  constructor(
    public dialogRef: MatDialogRef<ModalHostMonitorComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
  ) { 
    this.hostIp = this.data.hostIp;
    this.srcIframe = 'https://localhost:3000/d-solo/d45Ne8K4z/' + this.hostIp + '?orgId=1&from=1671179299139&to=1671200899140&theme=light&panelId=2';
  }

  ngOnInit(): void {
    
  }

  closeDialog() {
    this.dialogRef.close();
  }

}
