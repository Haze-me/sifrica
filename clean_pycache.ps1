Clear-Host
Write-Host "Cleaning __pycache__ folders..." -ForegroundColor Cyan

$folders = Get-ChildItem -Path . -Directory -Recurse -Force -ErrorAction SilentlyContinue |
Where-Object {
    $_.Name -eq '__pycache__' -and
    $_.FullName -notmatch '\\env\\'
}

$total = $folders.Count
if ($total -eq 0) {
    Write-Host "✅ No __pycache__ folders found." -ForegroundColor Green
    return
}

$deleted = 0
$skipped = 0
$index = 0

foreach ($folder in $folders) {
    $index++
    $percent = [math]::Round(($index / $total) * 100)
    $bar = ('#' * ($percent / 5)).PadRight(20)

    Write-Host -NoNewline "`r[$bar] $percent% -> $($folder.FullName)" -ForegroundColor Yellow

    try {
        Remove-Item $folder.FullName -Recurse -Force -ErrorAction Stop
        $deleted++
    } catch {
        $skipped++
    }
    Start-Sleep -Milliseconds 50
}

Write-Host "`nDone!"
Write-Host " Deleted: $deleted" -ForegroundColor Green
Write-Host "Skipped: $skipped" -ForegroundColor Red
