import wikipedia


# ==========================================
# DEEP SEARCH
# ==========================================

def deep_search(query):

    try:

        # CLEAN QUERY
        query = query.lower()

        query = query.replace(
            "pilot",
            ""
        )

        query = query.strip()

        # SEARCH BEST MATCH
        results = wikipedia.search(
            query
        )

        if not results:

            return (
                "Sorry sir, "
                "I could not find information."
            )

        # TAKE FIRST RESULT
        best_result = results[0]

        # GET SUMMARY
        answer = wikipedia.summary(

            best_result,

            sentences=2

        )

        return answer

    except Exception as e:

        print(
            "Search Error:",
            e
        )

        return (
            "Sorry sir, "
            "I could not find information."
        )