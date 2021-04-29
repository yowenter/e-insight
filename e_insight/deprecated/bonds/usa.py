import requests
from datetime import datetime
from e_insight.lib.cache import cache

from xml.dom.minidom import parseString


@cache(3600)
def fetch_usa_treasury_resp():
    cur_month = datetime.now().month
    cur_year = datetime.now().year

    url = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%20{month}%20and%20year(NEW_DATE)%20eq%20{year}".format(
        month=cur_month, year=cur_year)

    resp = requests.get(url).text
    return resp


def get_bond(yield_term):
    tree = parseString(fetch_usa_treasury_resp())
    ele = tree.getElementsByTagName("entry")[-1].getElementsByTagName("content")[0]
    rate = ele.getElementsByTagName("m:properties")[0].getElementsByTagName("d:%s" % yield_term)[0].childNodes[0].data
    return float(rate)


# 十年期国债收益率 解析

"""
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<feed xml:base="http://data.treasury.gov/Feed.svc/" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns="http://www.w3.org/2005/Atom">
  <title type="text">DailyTreasuryYieldCurveRateData</title>
  <id>http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData</id>
  <updated>2020-07-09T15:10:18Z</updated>
  <link rel="self" title="DailyTreasuryYieldCurveRateData" href="DailyTreasuryYieldCurveRateData" />
  <entry>
    <id>http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(7633)</id>
    <title type="text"></title>
    <updated>2020-07-09T15:10:18Z</updated>
    <author>
      <name />
    </author>
    <link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(7633)" />
    <category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" />
    <content type="application/xml">
      <m:properties>
        <d:Id m:type="Edm.Int32">7633</d:Id>
        <d:NEW_DATE m:type="Edm.DateTime">2020-07-01T00:00:00</d:NEW_DATE>
        <d:BC_1MONTH m:type="Edm.Double">0.12</d:BC_1MONTH>
        <d:BC_2MONTH m:type="Edm.Double">0.12</d:BC_2MONTH>
        <d:BC_3MONTH m:type="Edm.Double">0.14</d:BC_3MONTH>
        <d:BC_6MONTH m:type="Edm.Double">0.17</d:BC_6MONTH>
        <d:BC_1YEAR m:type="Edm.Double">0.16</d:BC_1YEAR>
        <d:BC_2YEAR m:type="Edm.Double">0.17</d:BC_2YEAR>
        <d:BC_3YEAR m:type="Edm.Double">0.19</d:BC_3YEAR>
        <d:BC_5YEAR m:type="Edm.Double">0.31</d:BC_5YEAR>
        <d:BC_7YEAR m:type="Edm.Double">0.52</d:BC_7YEAR>
        <d:BC_10YEAR m:type="Edm.Double">0.69</d:BC_10YEAR>
        <d:BC_20YEAR m:type="Edm.Double">1.2</d:BC_20YEAR>
        <d:BC_30YEAR m:type="Edm.Double">1.43</d:BC_30YEAR>
        <d:BC_30YEARDISPLAY m:type="Edm.Double">1.43</d:BC_30YEARDISPLAY>
      </m:properties>
    </content>
  </entry>
  <entry>
    <id>http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(7634)</id>
    <title type="text"></title>
    <updated>2020-07-09T15:10:18Z</updated>
    <author>
      <name />
    </author>
    <link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(7634)" />
    <category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" />
    <content type="application/xml">
      <m:properties>
        <d:Id m:type="Edm.Int32">7634</d:Id>
        <d:NEW_DATE m:type="Edm.DateTime">2020-07-02T00:00:00</d:NEW_DATE>
        <d:BC_1MONTH m:type="Edm.Double">0.13</d:BC_1MONTH>
        <d:BC_2MONTH m:type="Edm.Double">0.14</d:BC_2MONTH>
        <d:BC_3MONTH m:type="Edm.Double">0.14</d:BC_3MONTH>
        <d:BC_6MONTH m:type="Edm.Double">0.16</d:BC_6MONTH>
        <d:BC_1YEAR m:type="Edm.Double">0.16</d:BC_1YEAR>
        <d:BC_2YEAR m:type="Edm.Double">0.16</d:BC_2YEAR>
        <d:BC_3YEAR m:type="Edm.Double">0.19</d:BC_3YEAR>
        <d:BC_5YEAR m:type="Edm.Double">0.29</d:BC_5YEAR>
        <d:BC_7YEAR m:type="Edm.Double">0.5</d:BC_7YEAR>
        <d:BC_10YEAR m:type="Edm.Double">0.68</d:BC_10YEAR>
        <d:BC_20YEAR m:type="Edm.Double">1.2</d:BC_20YEAR>
        <d:BC_30YEAR m:type="Edm.Double">1.43</d:BC_30YEAR>
        <d:BC_30YEARDISPLAY m:type="Edm.Double">1.43</d:BC_30YEARDISPLAY>
      </m:properties>
    </content>
  </entry>
  <entry>
    <id>http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(7635)</id>
    <title type="text"></title>
    <updated>2020-07-09T15:10:18Z</updated>
    <author>
      <name />
    </author>
    <link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(7635)" />
    <category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" />
    <content type="application/xml">
      <m:properties>
        <d:Id m:type="Edm.Int32">7635</d:Id>
        <d:NEW_DATE m:type="Edm.DateTime">2020-07-06T00:00:00</d:NEW_DATE>
        <d:BC_1MONTH m:type="Edm.Double">0.12</d:BC_1MONTH>
        <d:BC_2MONTH m:type="Edm.Double">0.14</d:BC_2MONTH>
        <d:BC_3MONTH m:type="Edm.Double">0.15</d:BC_3MONTH>
        <d:BC_6MONTH m:type="Edm.Double">0.16</d:BC_6MONTH>
        <d:BC_1YEAR m:type="Edm.Double">0.16</d:BC_1YEAR>
        <d:BC_2YEAR m:type="Edm.Double">0.16</d:BC_2YEAR>
        <d:BC_3YEAR m:type="Edm.Double">0.19</d:BC_3YEAR>
        <d:BC_5YEAR m:type="Edm.Double">0.31</d:BC_5YEAR>
        <d:BC_7YEAR m:type="Edm.Double">0.51</d:BC_7YEAR>
        <d:BC_10YEAR m:type="Edm.Double">0.69</d:BC_10YEAR>
        <d:BC_20YEAR m:type="Edm.Double">1.21</d:BC_20YEAR>
        <d:BC_30YEAR m:type="Edm.Double">1.45</d:BC_30YEAR>
        <d:BC_30YEARDISPLAY m:type="Edm.Double">1.45</d:BC_30YEARDISPLAY>
      </m:properties>
    </content>
  </entry>
  <entry>
    <id>http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(7636)</id>
    <title type="text"></title>
    <updated>2020-07-09T15:10:18Z</updated>
    <author>
      <name />
    </author>
    <link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(7636)" />
    <category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" />
    <content type="application/xml">
      <m:properties>
        <d:Id m:type="Edm.Int32">7636</d:Id>
        <d:NEW_DATE m:type="Edm.DateTime">2020-07-07T00:00:00</d:NEW_DATE>
        <d:BC_1MONTH m:type="Edm.Double">0.12</d:BC_1MONTH>
        <d:BC_2MONTH m:type="Edm.Double">0.14</d:BC_2MONTH>
        <d:BC_3MONTH m:type="Edm.Double">0.15</d:BC_3MONTH>
        <d:BC_6MONTH m:type="Edm.Double">0.17</d:BC_6MONTH>
        <d:BC_1YEAR m:type="Edm.Double">0.15</d:BC_1YEAR>
        <d:BC_2YEAR m:type="Edm.Double">0.16</d:BC_2YEAR>
        <d:BC_3YEAR m:type="Edm.Double">0.19</d:BC_3YEAR>
        <d:BC_5YEAR m:type="Edm.Double">0.29</d:BC_5YEAR>
        <d:BC_7YEAR m:type="Edm.Double">0.48</d:BC_7YEAR>
        <d:BC_10YEAR m:type="Edm.Double">0.65</d:BC_10YEAR>
        <d:BC_20YEAR m:type="Edm.Double">1.15</d:BC_20YEAR>
        <d:BC_30YEAR m:type="Edm.Double">1.38</d:BC_30YEAR>
        <d:BC_30YEARDISPLAY m:type="Edm.Double">1.38</d:BC_30YEARDISPLAY>
      </m:properties>
    </content>
  </entry>
  <entry>
    <id>http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(7637)</id>
    <title type="text"></title>
    <updated>2020-07-09T15:10:18Z</updated>
    <author>
      <name />
    </author>
    <link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(7637)" />
    <category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme" />
    <content type="application/xml">
      <m:properties>
        <d:Id m:type="Edm.Int32">7637</d:Id>
        <d:NEW_DATE m:type="Edm.DateTime">2020-07-08T00:00:00</d:NEW_DATE>
        <d:BC_1MONTH m:type="Edm.Double">0.11</d:BC_1MONTH>
        <d:BC_2MONTH m:type="Edm.Double">0.13</d:BC_2MONTH>
        <d:BC_3MONTH m:type="Edm.Double">0.15</d:BC_3MONTH>
        <d:BC_6MONTH m:type="Edm.Double">0.17</d:BC_6MONTH>
        <d:BC_1YEAR m:type="Edm.Double">0.15</d:BC_1YEAR>
        <d:BC_2YEAR m:type="Edm.Double">0.16</d:BC_2YEAR>
        <d:BC_3YEAR m:type="Edm.Double">0.19</d:BC_3YEAR>
        <d:BC_5YEAR m:type="Edm.Double">0.3</d:BC_5YEAR>
        <d:BC_7YEAR m:type="Edm.Double">0.49</d:BC_7YEAR>
        <d:BC_10YEAR m:type="Edm.Double">0.67</d:BC_10YEAR>
        <d:BC_20YEAR m:type="Edm.Double">1.16</d:BC_20YEAR>
        <d:BC_30YEAR m:type="Edm.Double">1.39</d:BC_30YEAR>
        <d:BC_30YEARDISPLAY m:type="Edm.Double">1.39</d:BC_30YEARDISPLAY>
      </m:properties>
    </content>
  </entry>
</feed>
"""
