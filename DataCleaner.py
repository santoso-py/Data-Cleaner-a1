# ga semua task ada di versi ini, ini lebih ke versi umum, bisa ditambahkan dengan functin lainnhya
# hanya singel file py, tidak ada file main.py , dan module lainnya

import sys
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox, QProgressBar, QLabel, QInputDialog
from PyQt6.QtCore import QTimer
from datetime import datetime

class DataCleaner(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # File and folder selection
        self.file_button = QPushButton("Select File", self)
        self.file_button.clicked.connect(self.select_input_file)
        layout.addWidget(self.file_button)

        self.folder_button = QPushButton("Select Output Folder", self)
        self.folder_button.clicked.connect(self.select_output_folder)
        layout.addWidget(self.folder_button)

        # Progress bar
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        # Log output
        self.log_label = QLabel("Log Output:", self)
        layout.addWidget(self.log_label)

        # Start button
        self.start_button = QPushButton("Start Processing", self)
        self.start_button.clicked.connect(self.start_processing)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.setWindowTitle("Data Cleaner")
        self.setGeometry(100, 100, 400, 200)

    def select_input_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File", "", "Excel Files (*.xlsx *.csv)")
        if file_path:
            self.input_file = file_path
            self.log_label.setText(f"Selected File: {file_path}")

    def select_output_folder(self):
        folder_dialog = QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.output_folder = folder_path
            self.log_label.setText(f"Selected Folder: {folder_path}")

    def start_processing(self):
        self.progress_bar.setValue(0)
        self.process_data()
        self.progress_bar.setValue(100)
        QMessageBox.information(self, "Processing Complete", "Data cleaning is done!")

    def process_data(self):
        # Load file
        if self.input_file.endswith(".csv"):
            df = pd.read_csv(self.input_file)
        else:
            df = pd.read_excel(self.input_file)

        # Save unfiltered data
        unfilter_df = df.copy()

        # Handling null values
        df = self.handle_null_values(df)

        # Check outliers
        df, finding_df = self.detect_outliers(df)

        # Check type anomalies
        df, type_finding_df = self.check_type_anomalies(df)

        # Merge all findings
        finding_df = pd.concat([finding_df, type_finding_df], ignore_index=True)

        # Convert text to uppercase
        df = self.handle_uppercase(df)

        # Save output
        output_path = f"{self.output_folder}/cleaned_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
        with pd.ExcelWriter(output_path) as writer:
            unfilter_df.to_excel(writer, sheet_name="Unfilter", index=False)
            df.to_excel(writer, sheet_name="Hygiene", index=False)
            finding_df.to_excel(writer, sheet_name="Finding", index=False)

        self.log_label.setText(f"File saved: {output_path}")
#Batas proses
    def handle_null_values(self, df):
        null_columns = df.isnull().sum()
        for col, null_count in null_columns.items():
            if null_count > 0:
                value, ok = QInputDialog.getItem(self, "Handle Null Values", f"How to handle null values in '{col}'?", 
                                                 ["Keep Null", "-", "Fill with Mean", "Custom"], 0, False)
                if ok:
                    if value == "Keep Null":
                        df[col] = df[col]
                    elif value == "-":
                        df[col] = df[col].fillna("-")
                    elif value == "Fill with Mean" and df[col].dtype in ['int64', 'float64']:
                        df[col] = df[col].fillna(df[col].mean())
                    elif value == "Custom":
                        custom_value, ok = QInputDialog.getText(self, "Custom Value", f"Enter custom value for nulls in '{col}':")
                        if ok:
                            df[col] = df[col].fillna(custom_value)
        return df

    def detect_outliers(self, df):
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        finding_df = pd.DataFrame()
        
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            if not outliers.empty:
                outliers["Note"] = "Outlier"
                finding_df = pd.concat([finding_df, outliers])

                # Remove outliers from hygiene dataset
                df = df[~df.index.isin(outliers.index)]

        return df, finding_df

    def check_type_anomalies(self, df):
        finding_df = pd.DataFrame()
        for col in df.columns:
            if df[col].dtype == 'object':  # Cek hanya untuk kolom object
                for idx, val in df[col].items():
                    if isinstance(val, str):
                        # Jika kolom numerik tapi ada string
                        if col.lower() in ["price", "quantity"] and not val.isnumeric():
                            finding_df = pd.concat([finding_df, df.loc[[idx]]], ignore_index=True)
                            finding_df.loc[idx, "Note"] = "Tipe Data Anomaly"
                            df.drop(idx, inplace=True)

        return df, finding_df

    def handle_uppercase(self, df):
        reply = QMessageBox.question(self, "Uppercase All Text", "Do you want to convert all text to uppercase?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)
        return df


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cleaner = DataCleaner()
    cleaner.show()
    sys.exit(app.exec())
