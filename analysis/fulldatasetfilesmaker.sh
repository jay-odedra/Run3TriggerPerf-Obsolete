for i in {1..8}
do
dasgoclient --query "file dataset=/EphemeralZeroBias$i/ytakahas-Winter21_Trigger_20211207-30e4efebaefe52740b9ca928c2409cd7/USER instance=prod/phys03" > "fulldatafilenames$i.txt"
done
	
