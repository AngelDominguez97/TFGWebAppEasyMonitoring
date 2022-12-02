import { TestBed } from '@angular/core/testing';

import { LastcheckService } from './lastcheck.service';

describe('LastcheckService', () => {
  let service: LastcheckService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LastcheckService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
