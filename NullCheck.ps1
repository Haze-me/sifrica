$nullByteFound = $false

Get-ChildItem -Path . -Recurse -Include *.py -File | Where-Object {
    # Exclude any files under folders named 'env'
    $_.FullName -notmatch "\\env\\"
} | ForEach-Object {
    $file = $_.FullName
    Write-Host "Checking: $file" -ForegroundColor Cyan

    try {
        $content = Get-Content -Raw -Encoding Byte -ErrorAction Stop $file

        if ($content -contains 0) {
            Write-Host "❌ Null byte found in $file" -ForegroundColor Red
            $nullByteFound = $true
        }
    } catch {
        Write-Host "⚠️ Could not read $file due to error: $_" -ForegroundColor Yellow
    }
}

if ($nullByteFound) {
    Write-Host "`n❌ Null bytes were found in one or more files. Please clean them before running your app." -ForegroundColor Red
    exit 1
} else {
    Write-Host "`n✅ No null bytes found in any Python files." -ForegroundColor Green
    exit 0
}
