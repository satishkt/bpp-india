[[ -f "bpp.json" ]] && rm "bpp.json"
mongoexport --verbose --host 54.148.179.83 --port 27017 --db scrapy --collection bpp_india --out bpp.json
