


# Define the LDES
Write-Host "Defining the LDES..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.test.az.aquafin.be/ldes/admin/api/v1/eventstreams" -ContentType "text/turtle" -InFile ".\overstort-meting-raw.ttl"

# Wait to allow the previous step to finish
Start-Sleep -Seconds 5

# Define views for observation
Write-Host "Defining views..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.test.az.aquafin.be/ldes/admin/api/v1/eventstreams/overstort-meting-raw/views" -ContentType "text/turtle" -InFile ".\overstort.overstort-meting-raw-by-page.ttl"
Start-Sleep -Seconds 5


# Define pipelines
Write-Host "Defining pipelines..."
Invoke-RestMethod -Method Post -Uri "https://ldio-overstort.test.az.aquafin.be/admin/api/v1/pipeline" -ContentType "application/yaml" -InFile ".\overstort-meting-raw.yml"
Start-Sleep -Seconds 5
