import { useAtom } from 'jotai'
import {  XIcon } from 'lucide-react';
import { screenshotAtom } from 'state'

export default function Screenshot() {
    const [screenshot, setScreenshot] = useAtom(screenshotAtom);
    return (
        <div
            className='flex h-full items-center bg-background'
        >
            <div className='relative mx-auto'>
                <XIcon
                    onClick={()=> setScreenshot('')}
                    className='absolute text-zinc-600 dark:text-zinc-400 right-1 top-1 cursor-pointer' />
                <img
                    className='mx-auto object-contain  h-64 w-64  rounded-lg text-center text-zinc-600 shadow-lg dark:bg-zinc-800'
                    src={screenshot}
                />
            </div>
        </div>
    )
}
