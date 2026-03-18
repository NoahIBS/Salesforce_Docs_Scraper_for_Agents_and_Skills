<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_seo.htm&language=en_US&type=5 -->

# SEO Page Properties for Landing Pages in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# SEO Page Properties for Landing Pages in Marketing Cloud Next

To improve search engine optimization (SEO), use head tags to add structured data to your landing page. Including structured data provides more control over how your landing page and its information looks in search results.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Structured Data

Use structured data to provide page details in a standardized format to search engines so that they understand the content and meaning of a web page. You can use structured data to define thumbnail images, carousels, knowledge boxes, and more.

To add structured data to a page, add the `<script>` tag with the `application/ld+json` type attribute to the Edit Head Tags section. Then provide the page details that you want to highlight. For examples of using structured data, see the [structured data search gallery from Google](https://developers.google.com/search/docs/appearance/structured-data/search-gallery).

You can use only JSON-LD formatting for structured data on a landing page. Head tags don’t support JavaScript.

## Head Tags

For security purposes, you can use only certain tags, attributes, and values on a landing page.

Allowed Tags | Allowed Attributes  
---|---  
<link> | `as`, `charset`, `crossorigin`, `disabled`, `href`, `hreflang`, `id`, `import`, `integrity`, `media`, `rel`, `relList`, `rev`, `sheet`, `sizes`, `target`, `title`, `type` For `rel`, the allowed values are alternate, apple-touch-icon, apple-touch-icon-precomposed, apple-touch-startup-image, author, bookmark, canonical, external, help, icon, license, manifest, mask-icon, next, nofollow, noopener, noreferrer, pingback, prefetch, preload, prev, search, shortcut icon, stylesheet, and tag.  
<meta> | `charset`, `content`, `http-equiv`, `name`, `property`, `scheme` For `http-equiv`, the allowed values are cleartype, content-type, content-language, and default-style.You can use the attribute `http-equiv="X-UA-Compatible"` only in combination with `content="IE=Edge"`.  
<script> |  `type` For `type`, the allowed value is application/ld+json.
