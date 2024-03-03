import {format} from 'date-fns'
import {es} from 'date-fns/locale'

export default function CurrentDateFormatted () {
    return format(new Date(), "dd MMM yyyy",{locale: es});
}
