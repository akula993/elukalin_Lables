[Setup]
AppName=Elukalin
AppVersion=1.1
DefaultDirName={pf}\Elukalin
OutputDir=D:\project\elukalin2\Elukalin\build
OutputBaseFilename=setup

[Files]
Source: "D:\project\elukalin2\Elukalin\build\elukalin\elukalin.exe"; DestDir: "{app}"
Source: "D:\project\elukalin2\Elukalin\main.py"; DestDir: "{app}"

[Icons]
Name: "{group}\{cm:UninstallProgram,{#AppName}}"; Filename: "{uninstallexe}"
