import { NgModule } from "@angular/core";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatPaginatorModule } from "@angular/material/paginator";
import { MatSortModule } from "@angular/material/sort";
import { MatTableModule } from "@angular/material/table";
import { MatInputModule } from "@angular/material/input"
import { MatDialogModule } from "@angular/material/dialog";

@NgModule({
    exports: [
        MatTableModule,
        MatPaginatorModule,
        MatSortModule,
        MatFormFieldModule,
        MatInputModule,
        MatDialogModule
    ]
})
export class MaterialModule {

}