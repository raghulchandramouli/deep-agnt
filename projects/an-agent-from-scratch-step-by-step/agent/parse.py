def text_blocks(response):
    results = []

    if "content" not in response:
        return results

    for block in response["content"]:
        if block["type"] == 'text':
            results.append(block['text'])

    return results


def text_of(response):

    blocks = text_blocks(response)

    results = "\n".join(blocks)

    results = results.strip()

    return results
