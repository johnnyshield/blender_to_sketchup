#Get content from file
$outfilename = "C:\Temp\Test.dae"

#Get directory
$files = Get-ChildItem "C:\Temp\Test" -Filter *.dae

# XML tags to search for in source files
$firstString = "<geometry id="
$secondString = "</geometry>"
$thirdString = "<node id="
$fourthString = "</node>"

#Regex pattern to compare two strings
$pattern = "$firstString(.*?)$secondString"
$pattern2 = "$thirdString(.*?)$fourthString"

foreach ($f in $files){
    #Get content from file
    $file = Get-Content $f.FullName

    #Perform the opperation
    $result = [regex]::Match($file,$pattern).Groups[1].Value
    $geom = $firstString + $result + $secondString
    
    $result2 = [regex]::Match($file,$pattern2).Groups[1].Value
    $nodeinfo = $thirdString + $result2 + $fourthString

    (Get-Content $outfilename) | 
        Foreach-Object {
            $_ # send the current line to output
            if ($_ -match '<visual_scene id="myscene">') 
            {
                #Add Lines after the selected pattern 
                $nodeinfo
            }
            if ($_ -match '<library_geometries>') 
            {
                #Add Lines after the selected pattern 
                $geom
            }
        } | Set-Content $outfileName
}

