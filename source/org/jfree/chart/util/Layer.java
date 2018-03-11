/**
 * ----------
 * Layer.java
 * ----------
 * (C) Copyright 2003-2007, by Object Refinery Limited.
 *
 * Original Author:  David Gilbert (for Object Refinery Limited);
 * Contributor(s):   -;
 *
 * $Id: Layer.java,v 1.4 2005/10/18 13:18:34 mungady Exp $
 *
 * Changes:
 * --------
 * 17-Sep-2003 : Version 1 (DG);
 * 20-Jun-2007 : Copied from JCommon (DG);
 * 
 */

package org.jfree.chart.util;

import java.io.ObjectStreamException;
import java.io.Serializable;

/**
 * Used to indicate either the foreground or background layer.
 */
public final class Layer implements Serializable {

    /** For serialization. */
    private static final long serialVersionUID = -1470104570733183430L;
    
    /** Foreground. */
    public static final Layer FOREGROUND = new Layer("Layer.FOREGROUND");

    /** Background. */
    public static final Layer BACKGROUND = new Layer("Layer.BACKGROUND");

    /** The name. */
    private String name;

    /**
     * Private constructor.
     *
     * @param name  the name.
     */
    private Layer(String name) {
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
        if (!(obj instanceof Layer)) {
            return false;
        }

        Layer layer = (Layer) obj;
        if (!this.name.equals(layer.name)) {
            return false;
        }

        return true;

    }

    /**
     * Returns a hash code value for the object.
     *
     * @return the hashcode
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
        Layer result = null;
        if (this.equals(Layer.FOREGROUND)) {
            result = Layer.FOREGROUND;
        }
        else if (this.equals(Layer.BACKGROUND)) {
            result = Layer.BACKGROUND;
        }
        return result;
    }
    
}

