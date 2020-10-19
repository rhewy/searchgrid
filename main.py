# ==============================================================================
# File             : main.py
#
# Current Author   : Robert Hewlett
#
# Previous Author  : None
#
# Contact Info     : rob.hewy@gmail.com
#
# Purpose          : Demo loops and files
#
# Dependencies     : None ... yet
#
# Modification Log :
#    --> Created 2020-10-18 (rh)
#    --> Updated YYYY-MM-DD (fl)
#
# =============================================================================
# ===================================
# File extentions
# ===================================
prjExt = '.prj'
csvtExt = '.csvt'
csvExt = '.csv'
# ===================================
# Constants and defaults
# ===================================
inFileName = 'grid_in.txt'
csvFileName = 'grid_out.csv'
# ==================================================
# Create geocsv companion file based on output name
# ==================================================
projFileName = csvFileName.replace(csvExt, prjExt)
csvtFileName = csvFileName.replace(csvExt, csvtExt)
# ===================================
# Start the pk-id at 1
# ===================================
id = 1
# ===================================
# Seed the companion files 
# ===================================
with open(csvtFileName, 'w') as csvtFile, open(projFileName, 'w') as prjFile:
    csvtFile.write('Integer,WKT')
    prjFile.write('EPSG:26910')
# =======================================
# Process the grid file making WKT lines 
# ======================================
with open(csvFileName, 'w') as csvFile, open(inFileName, 'r') as inFile:
    csvFile.write('id,geom\n')
    for line in inFile:
        # =====================================================
        # Get the grid info: starts, intervals and iterations
        # ====================================================
        xStart = float(line)
        yStart = float(inFile.readline())
        xInterval = float(inFile.readline())
        yInterval = float(inFile.readline())
        interations = int(inFile.readline())
        # =====================================================
        # punch out the start
        # ====================================================
        csvFile.write(f'{id},\"LINESTRING({xStart} {yStart},')
        for i in range(interations):
            # ====================================================
            # punch out the coordinates for the grid pattern
            # ====================================================
            csvFile.write(f'{xStart} {yStart+yInterval},')
            csvFile.write(f'{xStart+xInterval} {yStart+yInterval},')
            csvFile.write(f'{xStart+xInterval} {yStart},')
            csvFile.write(f'{xStart+2*xInterval} {yStart}')
            # ===================================================
            # The last coordinate does not need a comma
            # ===================================================
            if i < interations - 1:
                csvFile.write(',')
            xStart += 2*xInterval
        # ===================================================
        # pClose off the WKT linestring
        # ===================================================
        csvFile.write(')\"\n')
    # ============================================================
    # increase the pk-id if there is another grid left to process
    # ============================================================
    id +=1
print('Done ...')



