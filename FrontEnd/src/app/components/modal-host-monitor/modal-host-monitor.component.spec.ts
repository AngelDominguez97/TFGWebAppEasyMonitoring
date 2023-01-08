import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalHostMonitorComponent } from './modal-host-monitor.component';

describe('ModalHostMonitorComponent', () => {
  let component: ModalHostMonitorComponent;
  let fixture: ComponentFixture<ModalHostMonitorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ModalHostMonitorComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ModalHostMonitorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
