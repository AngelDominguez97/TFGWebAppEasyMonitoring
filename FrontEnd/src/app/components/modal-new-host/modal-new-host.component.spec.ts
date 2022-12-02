import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModalNewHostComponent } from './modal-new-host.component';

describe('ModalNewHostComponent', () => {
  let component: ModalNewHostComponent;
  let fixture: ComponentFixture<ModalNewHostComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ModalNewHostComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ModalNewHostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
