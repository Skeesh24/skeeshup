# Registry path
$registryPath = "HKCU:\Control Panel\Cursors"
$schemesPath = "HKCU:\Control Panel\Cursors\Schemes"

# Name of the cursor pack 
$cursorPackName = "SkeesherPunk"
$cursorPackPath = $args[0]

# Check if the "Schemes" key exists, create it if not
if (-not (Test-Path $schemesPath)) {
    New-Item -Path $schemesPath -Force
}

# Check if the cursors location folder exists, create it if not
if (-not (Test-Path $cursorPackPath)) {
    New-Item -Path $cursorPackPath -Force
}

# Define the cursor values
$cursorValues = @"
$cursorPackPath\$($args[1]),
$cursorPackPath\$($args[2]),
$cursorPackPath\$($args[3]),
$cursorPackPath\$($args[4]),
$cursorPackPath\$($args[5]),
$cursorPackPath\$($args[6]),
$cursorPackPath\$($args[7]),
$cursorPackPath\$($args[8]),
$cursorPackPath\$($args[9]),
$cursorPackPath\$($args[10]),
$cursorPackPath\$($args[11]),
$cursorPackPath\$($args[12]),
$cursorPackPath\$($args[13]),
$cursorPackPath\$($args[14]),
$cursorPackPath\$($args[15]),
"@

# Setting the default scheme in at cursor path
Set-ItemProperty -Path $registryPath -Name "(Default)" -Value $cursorPackName -Force

# Settiing the cursor values mapping at the cursorPackName scheme
Set-ItemProperty -Path $schemesPath -Name $cursorPackName -Value $cursorValues -Force