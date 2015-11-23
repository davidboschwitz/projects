/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dbosch.dancelights;

/**
 *
 * @author davidboschwitz
 */
public abstract class LightsRunnable implements Runnable {

    private final int index;

    LightsRunnable(int index) {
        this.index = index;
    }

    @Override
    public abstract void run();
    
    public int getIndex(){
        return index;
    }

}
