{
  "hero": {
    "title": "Multi-step monitoring XPath examples"
  },
  "title": "Multi-step monitoring XPath examples",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-examples",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-monitoring-xpath-examples"
}

This article features several examples for extracting content from XML responses using XPath. These XPath queries allow you inspect an XML response coming back from your API or web service as part of a [Multi-step API monitor](/support/kb/synthetic-monitoring/api-monitoring/multi-step). An XPath query defines which part of the XML response you are interested in - typically a value contained in one of the XML nodes. You can then take that extracted value and check whether it [satisfies certain conditions](/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions) (using assertions), or [store it in a variable](/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables) for later use.

The XPath version used in Multi-step API monitor setups is XPath 1.0, which means that functions introduced in higher XPath versions are not supported.

## Example 1: Plain XML

Consider an API or web service that can return information about a product inventory. When we send a request to that API, it will return data about one or more products. Suppose it returns this very basic XML document when we request data about product P-12345:

    <?xml version="1.0" encoding="utf-8"?>
      <Products>
        <ProductInfo Id="P-12345">
          <Name>Product 12345</Name>
          <Price>99.90</Price>
        </ProductInfo>
      </Products>

The root node is **Products**, and inside it is a single **ProductInfo** node that represents the product we requested. Inside it are a **Name** node and a **Price** node, both of which have some text content inside it.

As soon as we've received this XML document from the API, we can verify its content in order to monitor that the API is behaving correctly. For example, we could "navigate" through this document, all the way down to the **Name** node, to extract the name of the product. The following XPath query retrieves that value:

`/Products/ProductInfo/Name/text()`

Notice how this example mentions each node in the hierarchy to get to the **Name** node, and finally uses the **text()** function to retrieve the inner text of that **Name** node.

If we use this XPath query in a Multi-step API Assertion, we can verify that the value does indeed exist in the XML document, and that it has the value we expect it to have:

![](/img/content/scr-MSA-xpath-assertion-example.min.png)

## Example 2: A SOAP Envelope with prefixes

If your API is a SOAP webservice, the XML it returns may look similar to this:

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:product="http://myproduct.com">
        <soap:Body>
          <product:GetProductInfoResponse>
            <product:GetProductInfoResult>
              <product:ProductInfo Id="P-12345">
                <product:Name>Product 12345</product:Name>
                <product:Price>99.90</product:Price>
              </product:ProductInfo>
            </product:GetProductInfoResult>
          </product:GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

Notice how this XML document not only contains the usual *xmlns* namespace attributes you expect to see in a SOAP XML, but also a prefixed namespace **xmlns:product** that describes the inner nodes containing the product information. As a result, each and every node, starting from the **Envelope** all the way down to the product data, has a prefix. The SOAP **Envelope** and **Body** nodes are referred to using the **soap:** prefix, the **GetProductInfoResponse** node and all its inner nodes use the **product:** prefix.

This allows us to define an XPath query that has a fully qualified node selector for each node in the path we want to select. The following XPath query returns the value 99.90:

`/soap:Envelope/soap:Body/product:GetProductInfoResponse/product:GetProductInfoResult/product:ProductInfo/product:Price/text()`

Notice how we need to include each prefix for every node in our query. If we leave one out, the XPath query will fail because XPath 1.0 requires us to refer to each node's full name, including its prefix. Still, we can simplify this query quite a bit because there is only one product in the document, and only one **Price** node. Since there is no ambiguity here, we can navigate to the **Price** node straight away using the descendant operator //:

`//product:Price/text()`

Notice that we still need to include the **product:** prefix.

So far, we've extracted the inner text of a node. If you want to extract the value of an attribute (such as the Id attribute with value "P-12345") instead? You can just use the XPath @ operator. This XPath query returns the value P-12345:

`//product:ProductInfo/@Id`

## Example 3: SOAP data with multiple objects

In our previous example, there was no ambiguity because everything was prefixed, and there was just a single **product:ProductInfo** object in our XML document. But what if we have a SOAP method that returns a list of objects? Consider this XML document, which lists more than one product (just two to keep it short):

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:product="http://myproduct.com">
        <soap:Body>
          <product:GetProductInfoResponse>
            <product:GetProductInfoResult>
              <product:ProductInfo Id="P-12345">
                <product:Name>Product 12345</product:Name>
                <product:Price>99.90</product:Price>
              </product:ProductInfo>
              <product:ProductInfo Id="P-24680">
                <product:Name>Product 24680</product:Name>
                <product:Price>45.99</product:Price>
              </product:ProductInfo>
            </product:GetProductInfoResult>
          </product:GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

If we want to get to the very first product and select its price, we could use the following query that returns 99.90. Remember that XPath arrays are 1-based, so we'll use an index value of 1:

`//product:ProductInfo[1]/product:Price/text()`

Similary, we could select the last product's price, returning 45.99:

`//product:ProductInfo[last()]/product:Price/text()`

We could even select a product based on its Product **Id** attribute. This query finds a product with Id equals P-24680 and select its price - returning 45.99:

`//product:ProductInfo[@Id="P-24680"]/product:Price/text()`

## Example 4: XML data with empty prefixes

We'll use SOAP data again for this example, but it applies to any XML document with the same characteristics. In our previous SOAP examples, we were fortunate enough that each node had a prefix. But your API's XML response may be returning XML that doesn't include a prefix everywhere.  
In XPath 1.0, each node that is subject to a namespace must be specified including its prefix. This becomes difficult when some nodes have an empty prefix. You can't specify an empty prefix in an XPath query, so selecting those nodes gets tricky.

Consider the following XML, which has prefixes for the SOAP Envelope and Body, but not for the inner nodes. Notice that no additional namespace has been defined for the product nodes:

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
          <GetProductInfoResponse>
            <GetProductInfoResult>
              <ProductInfo Id="P-12345">
                <Name>Product 12345</Name>
                <Price>99.90</Price>
              </ProductInfo>
            </GetProductInfoResult>
          </GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

This still works as expected, because the nodes without a prefix are not subject to a namespace. This XPath query returns 99.90:

`//Price/text()`

Now let's look at a variation that does have an additional namespace. Notice the xmlns="http://myproduct.com" attribute at the root level, which doesn't specify a prefix (i.e. it has an empty prefix):

    <?xml version="1.0" encoding="utf-8"?>
      <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns="http://myproduct.com">
        <soap:Body>
          <GetProductInfoResponse>
            <GetProductInfoResult>
              <ProductInfo Id="P-12345">
                <Name>Product 12345</Name>
                <Price>99.90</Price>
              </ProductInfo>
            </GetProductInfoResult>
          </GetProductInfoResponse>
        </soap:Body>
      </soap:Envelope>

In this case, the inner nodes are subject to that namespace, but we can't select them in the ordinary way, because their namespace prefix is empty. Therefore, the following query doesn't work and simply returns an empty value:

`//Price/text()`

Unfortunately, there's no way to include an empty prefix in an XPath query. Thankfully, there's a way to avoid the empty prefix problem. We can use the XPath function **local-name()** that allows us to select a node using its name, without having to specify the prefix:

`//*[local-name()="Price"]/text()`

The structure of this query is:

`//` descendant operator: select all descendant nodes from the root  
`*` wildcard operator: any node, regardless of its node name  
`[local-name()="Price"]`: only select nodes that have a local name (i.e. excluding any prefix) equal to Price  
`text()`: select the inner text of the selected node(s)

Looking at our previous examples that had multiple ProductInfo nodes in the XML, we can combine several strategies for selecting the nodes we are interested in. This query selects the ProductInfo node with Id equals P-24680, and then gets the inner text of its Price node:

`//*[local-name()="ProductInfo"][@Id="P-24680"]/*[local-name()="Price"]/text()`

## Example 5: XPath functions

The previous examples used XPath queries to verify the existence of one or more nodes in an XML document and return the content of a node or node attribute. Aside from finding nodes and their contents, XPath also lets you execute certain functions. Keeping in mind that only XPath 1.0 functions are available, here are some examples:

| Function                                                                                                                                                                                                                                                                    | Example query                         | Value  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|--------|
| The **count()** function counts how many nodes are found using the argument you specify. It returns a numeric value you can use in an assertion. For example, you can set up an assertion that checks that the number of products returned is greater than or equal to 100. | count(//ProductInfo)                  | 2      |
| The **contains()** function checks whether the selected string value contains the substring you specify. Returns either True or False.                                                                                                                                      | contains(//ProductInfo/Name, "12345") | True   |
| The **sum()** function calculates the sum of the (numeric values) of the selected nodes.                                                                                                                                                                                    | sum(//ProductInfo/Price)              | 145.89 |
