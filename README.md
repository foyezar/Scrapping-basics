## robots.txt rules

1. Allow full access

User-agent: \*

Disallow:

If you find this in the robots.txt file of a website you’re trying to crawl, you’re in luck. This means all pages on the site are crawlable by bots.

2. Block all access

User-agent: \*

Disallow: /

You should steer clear from a site with this in its robots.txt. It states that no part of the site should be visited by using an automated crawler and violating this could mean legal trouble.

3. Partial access

User-agent: \*

Disallow: /folder/

User-agent: \*

Disallow: /file.html

Some sites disallow crawling only particular sections or files on their site. In such cases, you should direct your bots to leave the blocked areas untouched.

4. Crawl rate limiting

Crawl-delay: 11

This is used to limit crawlers from hitting the site too frequently. As frequent hits by crawlers could place unwanted stress on the server and make the site slow for human visitors, many sites add this line in their robots file. In this case, the site can be crawled with a delay of 11 seconds.

5. Visit time

Visit-time: 0400-0845

This tells the crawlers about hours when crawling is allowed. In this example, the site can be crawled between 04:00 and 08:45 UTC. Sites do this to avoid load from bots during their peak hours.

6. Request rate

Request-rate: 1/10

Some websites do not entertain bots trying to fetch multiple pages simultaneously. Request rate is used to limit this behavior. 1/10 as the value means the site allows crawlers to request one page every 10 seconds.

Web Scraping Best Practices: https://www.promptcloud.com/blog/web-scraping-best-practices/
