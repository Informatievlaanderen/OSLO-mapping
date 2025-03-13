


# Define the LDES
Write-Host "Defining the LDES..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.test.az.aquafin.be/ldes/admin/api/v1/eventstreams" -ContentType "text/turtle" -InFile ".\overstort-sensor.ttl"

# Wait to allow the previous step to finish
Start-Sleep -Seconds 5

# Define views for observation
Write-Host "Defining views..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.test.az.aquafin.be/ldes/admin/api/v1/eventstreams/overstort-sensor/views" -ContentType "text/turtle" -InFile ".\overstort.overstort-sensor-by-page.ttl"
Start-Sleep -Seconds 5


# Define pipelines
Write-Host "Defining pipelines..."
Invoke-RestMethod -Method Post -Uri "https://ldio-overstort.test.az.aquafin.be/admin/api/v1/pipeline" -ContentType "application/yaml" -InFile ".\overstort-sensor.yml"
Start-Sleep -Seconds 5
