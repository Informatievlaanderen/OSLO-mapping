#use powershell
#make sure you have Rest installed so you can execute rest commands
#do this on an Aquafin laptop or connect to the network using VPN
#change the directory in powershell to github-repo-path/definitions

# Function to find the target directory
function Find-TargetDirectory {
    param (
        [string]$targetFolder = "LDES Opzet AQF\definitions\PRD"
    )
    
    Write-Host "Searching for directory: $targetFolder"
    
    # Try to find the OSLO-mapping repository anywhere on common drives
    $drives = Get-PSDrive -PSProvider FileSystem | Select-Object -ExpandProperty Root
    $osloMappingPath = $null
    $found = $false
    
    foreach ($drive in $drives) {
        Write-Host "Searching on drive $drive..."
        # First try to find 'source\repos\OSLO-mapping' - the common GitHub location
        $repoPath = Get-ChildItem -Path $drive -Filter "OSLO-mapping" -Directory -Recurse -Depth 4 -ErrorAction SilentlyContinue | 
                    Where-Object { $_.FullName -like "*source\repos\OSLO-mapping*" } | 
                    Select-Object -First 1
        
        if ($repoPath) {
            $possiblePath = Join-Path -Path $repoPath.FullName -ChildPath "docs\_water\Overstort\$targetFolder"
            if (Test-Path -Path $possiblePath) {
                $osloMappingPath = $possiblePath
                $found = $true
                break
            }
        }
        
        # If not found in standard GitHub location, look for OSLO-mapping anywhere
        if (-not $found) {
            $repoPath = Get-ChildItem -Path $drive -Filter "OSLO-mapping" -Directory -Recurse -Depth 5 -ErrorAction SilentlyContinue | 
                        Select-Object -First 1
            
            if ($repoPath) {
                $possiblePath = Join-Path -Path $repoPath.FullName -ChildPath "docs\_water\Overstort\$targetFolder"
                if (Test-Path -Path $possiblePath) {
                    $osloMappingPath = $possiblePath
                    $found = $true
                    break
                }
            }
        }
        
        # If still not found, try to find the target folder directly
        if (-not $found) {
            $prdPath = Get-ChildItem -Path $drive -Filter "PRD" -Directory -Recurse -Depth 6 -ErrorAction SilentlyContinue | 
                        Where-Object { $_.FullName -like "*$targetFolder*" } | 
                        Select-Object -First 1
            
            if ($prdPath) {
                $parentPath = $prdPath.FullName
                if ($parentPath.EndsWith($targetFolder)) {
                    $osloMappingPath = $parentPath
                    $found = $true
                    break
                }
            }
        }
    }
    
    if ($found) {
        Write-Host "Found target directory: $osloMappingPath" -ForegroundColor Green
        return $osloMappingPath
    } else {
        Write-Host "Could not find the target directory automatically." -ForegroundColor Red
        Write-Host "Please clone the OSLO-mapping repository and ensure it contains: docs\_water\Overstort\$targetFolder" -ForegroundColor Yellow
        exit 1
    }
}

# Find and navigate to the target directory
try {
    $targetDir = Find-TargetDirectory
    Set-Location -Path $targetDir
    
    Write-Host "Directory set to: $targetDir" -ForegroundColor Green
# Define the LDES datastream
Write-Host "Defining the LDES..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.prd.az.aquafin.be/ldes/admin/api/v1/eventstreams" -ContentType "text/turtle" -InFile ".\overstort-event-cleansed.ttl"

# Wait to allow the previous step to finish
Start-Sleep -Seconds 5

# Define views for observation
Write-Host "Defining views..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.prd.az.aquafin.be/ldes/admin/api/v1/eventstreams/overstort-event-cleansed/views" -ContentType "text/turtle" -InFile ".\overstort.overstort-event-cleansed-by-page.ttl"
Start-Sleep -Seconds 5


# Define pipelines
Write-Host "Defining pipelines..."
Invoke-RestMethod -Method Post -Uri "https://ldio-overstort.prd.az.aquafin.be/admin/api/v1/pipeline" -ContentType "application/yaml" -InFile ".\overstort-event-cleansed.yaml"
Start-Sleep -Seconds 5

