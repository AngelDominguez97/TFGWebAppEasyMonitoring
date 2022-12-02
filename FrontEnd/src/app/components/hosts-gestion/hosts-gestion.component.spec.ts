import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HostsGestionComponent } from './hosts-gestion.component';

describe('HostsGestionComponent', () => {
  let component: HostsGestionComponent;
  let fixture: ComponentFixture<HostsGestionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HostsGestionComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HostsGestionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
