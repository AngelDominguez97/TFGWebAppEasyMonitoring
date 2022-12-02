import { Component, Inject, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { HostModel } from 'src/app/models/host.model';
import { HostService } from 'src/app/services/host/host.service';

@Component({
    selector: 'app-modal-host',
    templateUrl: './modal-host.component.html',
    styleUrls: ['./modal-host.component.css']
})
export class ModalHostComponent implements OnInit {

    updateHostForm!: FormGroup;
    hostName = '';
    hostIp = '';
    id = 0;
    userId = 0;
    noData = false;
    
    constructor(
        private hostService: HostService,
        public dialogRef: MatDialogRef<ModalHostComponent>,
        private fb: FormBuilder,
        @Inject(MAT_DIALOG_DATA) public data: any
    ) { 
        this.id = data.id;
        this.hostName = data.hostName;
        this.hostIp = data.hostIp;
        this.userId = data.userId;
    }


    ngOnInit() {
        this.updateHostForm = this.fb.group({
            id: [this.id, []],
            hostName: [this.hostName, []],
            hostIp: [this.hostIp, []],
            userId: [this.userId, []]
        });
    }

    closeDialog() {
        this.dialogRef.close();
    }

    updateHost(): void {
        if ((this.updateHostForm.value.hostName === null || this.updateHostForm.value.hostIp === null) || (this.updateHostForm.value.hostName === "" || this.updateHostForm.value.hostIp === "")) {
            this.noData = true;
        } else {
            this.noData = false;
            this.hostService.updateHost(this.updateHostForm.value).subscribe({
                next: (res: any) => {

                },
                error: (e) => {
                    // Redirigir a la pagina de error
                }
            });
        }
    }

}
