bpp-india
=========

Product Prices analysis for various online retail stores ( Amazon,Flipkart,Snapdeal,HomeShop18 etc.)
----------------------------------------------------------------------------------------------------
Billion Prices Project is an initiative by two MIT profs to compute inflation statistics from online prices of goods instead of physical sampling as done by BLS. We are replicating the same for India.

Using the same category of products that RBI uses, we mine various online stores for prices of goods on a daily basis.
We generate category indices for each category of products using appropriate weighting and then create a final inflation index.

Comparing All Store Analysis - https://s3-us-west-2.amazonaws.com/midsprojectoutput/compareall/part-00000

Comparing Flipkart & Amazon - https://s3-us-west-2.amazonaws.com/midsprojectoutput/compareamazonflipkart/part-00000

Comparing Snapdeal and FlipKart - https://s3-us-west-2.amazonaws.com/midsprojectoutput/comparelipkartsnapdeal/part-00000

Stores Sorted from Min to Max Price for a Product -

https://s3-us-west-2.amazonaws.com/midsprojectoutput/vendorpricesorted/part-00000
https://s3-us-west-2.amazonaws.com/midsprojectoutput/vendorpricesorted/part-00001
https://s3-us-west-2.amazonaws.com/midsprojectoutput/vendorpricesorted/part-00002
https://s3-us-west-2.amazonaws.com/midsprojectoutput/vendorpricesorted/part-00003

Store at which item is available at minimum price -

https://s3-us-west-2.amazonaws.com/midsprojectoutput/minprice/part-00000
https://s3-us-west-2.amazonaws.com/midsprojectoutput/minprice/part-00000
https://s3-us-west-2.amazonaws.com/midsprojectoutput/minprice/part-00000
https://s3-us-west-2.amazonaws.com/midsprojectoutput/minprice/part-00000







Essential Commodity Retail Price Analysis for various Items across different cities
----------------------------------------------------------------------------------------------------
The data is provided by Ministry of Consumer Affairs, Food and Public Distribution
We also analysed the commodity prices across various items ( rice/sugar/gasoline etc.) and the variation in prices across Tier 1 cities in India. The results are below

https://public.tableausoftware.com/views/bpp_wpi_0/PriceAnalysis?:embed=y&:display_count=no

Analysis using R
----------------------------------------------------------------------------------------------------

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-e3zv{font-weight:bold}
</style>
<table class="tg">
  <tr>
    <th class="tg-e3zv">CPI</th>
    <th class="tg-e3zv">Inflation</th>
  </tr>
  <tr>
    <td class="tg-031e">106.8312</td>
    <td class="tg-031e">"</td>
  </tr>
  <tr>
    <td class="tg-031e">137.511053</td>
    <td class="tg-031e">28.718065</td>
  </tr>
  <tr>
    <td class="tg-031e">133.878712</td>
    <td class="tg-031e">-2.641491</td>
  </tr>
  <tr>
    <td class="tg-031e">442.792329</td>
    <td class="tg-031e">230.741403</td>
  </tr>
  <tr>
    <td class="tg-031e">514.803536</td>
    <td class="tg-031e">16.262975</td>
  </tr>
  <tr>
    <td class="tg-031e">797.175041</td>
    <td class="tg-031e">54.850343</td>
  </tr>
  <tr>
    <td class="tg-031e">412.962419</td>
    <td class="tg-031e">-48.19677</td>
  </tr>
  <tr>
    <td class="tg-031e">823.945396</td>
    <td class="tg-031e">99.520673</td>
  </tr>
  <tr>
    <td class="tg-031e">455.254099</td>
    <td class="tg-031e">-44.747055</td>
  </tr>
  <tr>
    <td class="tg-031e">792.8606</td>
    <td class="tg-031e">74.157807</td>
  </tr>
  <tr>
    <td class="tg-031e">804.37898</td>
    <td class="tg-031e">1.452768</td>
  </tr>
  <tr>
    <td class="tg-031e">447.536169</td>
    <td class="tg-031e">-44.362523</td>
  </tr>
  <tr>
    <td class="tg-031e">477.174856</td>
    <td class="tg-031e">6.622635</td>
  </tr>
  <tr>
    <td class="tg-031e">1025.633529</td>
    <td class="tg-031e">114.938721</td>
  </tr>
  <tr>
    <td class="tg-031e">647.224839</td>
    <td class="tg-031e">-36.895117</td>
  </tr>
  <tr>
    <td class="tg-031e">749.369954</td>
    <td class="tg-031e">15.782014</td>
  </tr>
  <tr>
    <td class="tg-031e">832.454373</td>
    <td class="tg-031e">11.087236</td>
  </tr>
  <tr>
    <td class="tg-031e">463.089626</td>
    <td class="tg-031e">-44.37057</td>
  </tr>
  <tr>
    <td class="tg-031e">307.903021</td>
    <td class="tg-031e">-33.511138</td>
  </tr>
  <tr>
    <td class="tg-031e">977.612001</td>
    <td class="tg-031e">217.506466</td>
  </tr>
  <tr>
    <td class="tg-031e">699.300975</td>
    <td class="tg-031e">-28.468454</td>
  </tr>
  <tr>
    <td class="tg-031e">543.599912</td>
    <td class="tg-031e">-22.265243</td>
  </tr>
  <tr>
    <td class="tg-031e">1.839218</td>
    <td class="tg-031e">-99.66166</td>
  </tr>
</table>
