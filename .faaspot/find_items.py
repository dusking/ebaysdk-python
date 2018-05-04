
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from wrapper import endpoint

schema = {
    'required': ['keywords'],
    'properties':  {
        'keywords': {'type': 'string'},
        'page_size': {'type': 'integer'}
    }
}

@endpoint(schema)
def find_items(args):   
    keywords = args.get('keywords')
    page_size = args.get('page_size')
   
    appid = 'omerdusk-pricing-PRD-008f655c9-7cf91c5a'
    api = Connection(appid=appid, config_file=None)    
    paginationInput = {"entriesPerPage": str(page_size), "pageNumber" : "1"} if page_size else None    
    response = api.execute('findItemsAdvanced', {
        'keywords': keywords,
        'paginationInput': paginationInput})

    assert(response.reply.ack == 'Success')
    items = []
    for item in response.reply.searchResult.item:
        items.append({
            'title': item.title,
            'image': item.galleryURL,
            'price': item.sellingStatus.currentPrice.value,
            'currency': item.sellingStatus.currentPrice._currencyId,
            'condition': item.condition.conditionDisplayName
            })

    return items
