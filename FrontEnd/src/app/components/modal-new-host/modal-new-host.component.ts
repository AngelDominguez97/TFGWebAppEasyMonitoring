import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HostService } from 'src/app/services/host/host.service';
import { HostsGestionComponent } from '../hosts-gestion/hosts-gestion.component';

@Component({
  selector: 'app-modal-new-host',
  templateUrl: './modal-new-host.component.html',
  styleUrls: ['./modal-new-host.component.css']
})
export class ModalNewHostComponent implements OnInit {

  newHostForm!: FormGroup;
  hostName = '';
  hostIp = '';
  id = 0;
  userId = 0;
  noData = false;
  @ViewChild('closebutton') closebutton: any;
  constructor(
    private fb: FormBuilder,
    private hostService: HostService,
    private hostComponent: HostsGestionComponent
  ) { }

  ngOnInit(): void {
    this.newHostForm = this.fb.group({
      hostName: [null, Validators.required],
      hostIp: [null, Validators.required]
    });
  }

  createHost(): void {
    debugger;
    if ((this.newHostForm.value.hostName === null || this.newHostForm.value.hostIp === null) || (this.newHostForm.value.hostName === "" || this.newHostForm.value.hostIp === "")) {
      this.noData = true;
    } else {
      this.noData = false;
      this.hostService.createHost(this.newHostForm.value).subscribe({
        next: (res: any) => {
          this.closebutton.nativeElement.click();
          this.hostComponent.getHosts();
        },
        error: (e) => {
          // Redirigir a la pagina de error
        }
      });
    }
  }
}
