package io.datasearch.denguestore.query;

import org.geotools.data.Query;

/**
 * Query Object class.
 */
public class QueryObject {
    public String catalog;
    public Query query;
    public String schema;

    public QueryObject(String catalog, Query query, String schema) {
        this.catalog = catalog;
        this.query = query;
        this.schema = schema;
    }
}
