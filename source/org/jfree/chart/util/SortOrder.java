/**
  * --------------
 * SortOrder.java
 * --------------
 * (C) Copyright 2003-2007, by Object Refinery Limited.
 *
 * Original Author:  David Gilbert (for Object Refinery Limited);
 * Contributor(s):   -;
 *
 * $Id: SortOrder.java,v 1.6 2005/10/18 13:24:19 mungady Exp $
 *
 * Changes:
 * --------
 * 05-Mar-2003 : Version 1 (DG);
 * 13-Mar-2003 : Implemented Serializable (DG);
 * 27-Aug-2003 : Moved from JFreeChart --> JCommon (DG);
 * 29-Jul-2004 : Fixed error in readResolve() method (DG);
 * 20-Jun-2007 : Copied from JCommon (DG);
 * 
 */

package org.jfree.chart.util;

import java.io.ObjectStreamException;
import java.io.Serializable;

/**
 * Defines tokens used to indicate sorting order (ascending or descending).
 */
public final class SortOrder implements Serializable {

    /** For serialization. */
    private static final long serialVersionUID = -2124469847758108312L;
    
    /** Ascending order. */
    public static final SortOrder ASCENDING = new SortOrder(
            "SortOrder.ASCENDING");

    /** Descending order. */
    public static final SortOrder DESCENDING = new SortOrder(
            "SortOrder.DESCENDING");

    /** The name. */
    private String name;

    /**
     * Private constructor.
     *
     * @param name  the name.
     */
    private SortOrder(String name) {
        this.name = name;
    }

    /**
     * Returns a string representing the object.
     *
     * @return The string.
     */
    public String toString() {
        return this.name;
    }

    /**
     * Returns <code>true</code> if this object is equal to the specified 
     * object, and <code>false</code> otherwise.
     *
     * @param obj  the other object.
     *
     * @return A boolean.
     */
    public boolean equals(Object obj) {

        if (this == obj) {
            return true;
        }
        if (!(obj instanceof SortOrder)) {
            return false;
        }

        final SortOrder that = (SortOrder) obj;
        if (!this.name.equals(that.toString())) {
            return false;
        }

        return true;
    }
    
    /**
     * Returns a hash code value for the object.
     *
     * @return The hashcode
     */
    public int hashCode() {
        return this.name.hashCode();
    }

    /**
     * Ensures that serialization returns the unique instances.
     * 
     * @return The object.
     * 
     * @throws ObjectStreamException if there is a problem.
     */
    private Object readResolve() throws ObjectStreamException {
        if (this.equals(SortOrder.ASCENDING)) {
            return SortOrder.ASCENDING;
        }
        else if (this.equals(SortOrder.DESCENDING)) {
            return SortOrder.DESCENDING;
        }
        return null;
    }
}