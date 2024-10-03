import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true,
})
export class AppComponent {
  selectedFile: File | null = null;
  processedFileUrl: string | null = null;
  processing: boolean = false;

  constructor(private http: HttpClient) { }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onUpload() {
    if (!this.selectedFile) return;

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.processing = true;

    this.http.post('http://localhost:5000/upload', formData, { responseType: 'blob' })
      .subscribe(response => {
        const url = window.URL.createObjectURL(response);
        this.processedFileUrl = url;
        this.processing = false;
      }, error => {
        console.error('Erro ao processar PDF', error);
        this.processing = false;
      });
  }
}
